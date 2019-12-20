import numpy as np
import matplotlib.pyplot as plt

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, validation_curve, cross_val_score, KFold
from sklearn.metrics import accuracy_score, f1_score



def Rf_classification(X_train, y_train, X_test, y_test, tscv, score = 'accuracy'):
    """
    Random forest classification
    
    Parameters
    ----------
    
    Returns
    --------
    """
   
    seed = 1
        
    # Define a random classifier pipeline
    estimators = []
    estimators.append(('rf_clf', RandomForestClassifier()))
    pipeline = Pipeline(estimators)

    # Fixed parameters
    score = score
    tuning_param_range = [int(i) for i in np.linspace(10, 100, 10)]
    tuning_param = 'rf_clf__n_estimators'
    cv_schema = tscv


    # Tune hyper parameter using validation curve
    train_scores_val, cv_scores_val = validation_curve(
        pipeline, X_train, y_train, param_name = tuning_param, param_range = tuning_param_range,
        cv = cv_schema, scoring = score, n_jobs = -1)

    # Obtain the best value of the hyper parameter, with the best accuracy score
    best_param_val_rf = tuning_param_range[np.argmax(np.mean(cv_scores_val, axis=1))]
    best_rf_acc = max(np.mean(cv_scores_val, axis=1))
    
    pipeline.set_params(rf_clf__n_estimators = best_param_val_rf)
    pipeline.fit(X_train,y_train)
    y_pred = pipeline.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print ('rf classifer accuracy = %2.4f' %score)
    
    return y_pred, pipeline


def GBT_classification(X_train, y_train, X_test, y_test, tscv, ratio = None, score = 'f1_weighted'):
    """
    Gradient boosted trees classification
    
    Parameters
    ----------
    
    Returns
    --------
    """
 
    estimators = []
    if ratio :
        estimators.append(('XGB_clf', XGBClassifier(scale_pos_weight = ratio)))
    else :
        estimators.append(('XGB_clf', XGBClassifier()))
        
    gb_pipe = Pipeline(estimators)

    # Fixed parameters
    score = score
    n_splits = 3
    seed=0
    
    # CV schema
    cv_schema = tscv

    # Tune model against a single hyper parameter
    tuning_param = 'XGB_clf__n_estimators'
    tuning_param_range = [int(i) for i in np.linspace(10.0, 30.0, 5)]

    # Tune hyper parameter using validation curve
    train_scores_val, cv_scores_val = validation_curve(
        gb_pipe, X_train, y_train, param_name = tuning_param, param_range = tuning_param_range,
        cv = cv_schema, scoring = score, n_jobs = -1)

    # Obtain the best value of the hyper parameter
    best_param_val_GBT = tuning_param_range[np.argmax(np.mean(cv_scores_val, axis=1))]
    best_xgb_acc = max(np.mean(cv_scores_val, axis=1))
    #print(best_param_val_GBT)
    #print(best_xgb_acc)
    
    if ratio :
        optimal_xgb =  XGBClassifier(n_estimators=best_param_val_GBT, scale_pos_weight = ratio)
    else :
        optimal_xgb =  XGBClassifier(n_estimators=best_param_val_GBT)
        
    optimal_xgb.fit(X_train,y_train)
    xgb_pred = optimal_xgb.predict(X_test)
    acc_xgb = accuracy_score(y_test, xgb_pred)
    f1_xgb = f1_score(y_test, xgb_pred, average = "weighted")
    print("Gradient Boosted trees model accuracy score : " + str(acc_xgb))
    print("Gradient Boosted trees model F1 score : " + str(f1_xgb))
    
    return xgb_pred, optimal_xgb


def plot_confusion_matrix(y_true, y_pred, classes, title=None, cmap=plt.cm.Blues, figsize=(6,6)):
    """
    This function prints and plots the confusion matrix.
    
    Parameters
    ----------
    
    Returns
    --------
    """
    
    # Compute the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print(cm)

    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    
    # Show ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax