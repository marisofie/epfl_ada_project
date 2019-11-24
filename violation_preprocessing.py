# Functions for treating violations

import pandas as pd

def violation_separator(violations):
    '''
    Function that split the violations number from the violation description

    Parameters
    ----------

    violations: pandas.Series
        Violation column from dataframe with the different violations

    Returns
    -------
    violation_number: pandas.DataFrame
        DataFrame with separated violations
    '''

    #creating an empty dataframe in order to stock the violation numbers
    violation_number = pd.Series([])

    if type(violations) == str:
        #each different violation is separated by a ' | ' in a dataframe cell
        violations = violations.split(' | ')

        for violation in violations:
            #the index refers to the violation number
            index = "#" + violation.split('.')[0]
            #add 1 if there is a violation #.. and 0 if not.
            violation_number[index] = 1

    return violation_number


def violations_dataframe (separated_data, basic_data):

    '''
    Count violations by category

    Parameters
    ----------
    separated_data: pandas.DataFrame
        DataFrame with separated violations

    basic_data: pandas.DataFrame
        DataFrame with the original data

    Returns
    -------
    violation_data: pandas.DataFrame
        DataFrame with truth table for the violations (if they occured(1) or not(0))

    violation_counts: pandas.DataFrame
        DataFrame with grouped violations

    '''

    #columns creation
    critical = [("#" + str(num)) for num in range(1, 15)]
    serious = [("#" + str(num)) for num in range(15, 30)]
    minor = [("#" + str(num)) for num in range(30, 45)]
    minor.append("#70")

    # Create complete list of column names
    columns = critical + serious + minor

    # Create dataframe using column names, violation data and inspection ID
    violations_data = pd.DataFrame(separated_data, columns=columns)
    violations_data['inspection_id'] = basic_data.inspection_id
    violations_data['license'] = basic_data.license
    violations_data['inspection_type'] = basic_data.inspection_type
    violations_data['zip'] = basic_data.zip
    violation_data['risk'] = basic_data.risk
    violation_data['results'] = basic_data.results

    violation_counts = pd.DataFrame({
    "critical_count": violations_data[critical].sum(axis=1),
    "serious_count": violations_data[serious].sum(axis=1),
    "minor_count": violations_data[minor].sum(axis=1)
    })

    violation_counts['inspection_id'] = basic_data.inspection_id

    # Display selection of sums dataframe
    violation_counts.iloc[3:6]

    violation_counts = basic_data.merge(violation_counts, on = ['inspection_id'])

    #calculation of the proportion of type of count in order to normalize this variable.
    violation_counts['violations_count'] = violation_counts.critical_count + violation_counts.serious_count+violation_counts.minor_count

    #we ajust the count in order to have a proportion
    violation_counts['critical_count']=violation_counts['critical_count'].divide(violation_counts["violations_count"])
    violation_counts['serious_count']=violation_counts['serious_count'].divide(violation_counts["violations_count"])
    violation_counts['minor_count']=violation_counts['minor_count'].divide(violation_counts["violations_count"])

    violation_counts.fillna(0,inplace=True)


    return violations_data,violation_counts
