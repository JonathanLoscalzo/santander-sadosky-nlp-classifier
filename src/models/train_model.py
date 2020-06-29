from sklearn.metrics import balanced_accuracy_score

def fit_model(model, preprocess, X, y, fit_params={}):
    text_features = preprocess.transform(X)
    model.fit(text_features, y, **fit_params)
    return model

def get_preds(model, preprocess, X):
    text_features = preprocess.transform(X)
    return model.predict(text_features)

def get_metrics(model, preprocess, X_train, y_train, X_test, y_test):
    def _callback(model, preprocess, X, y, stage='Train'):
        y_pred = get_preds(model, preprocess, X)
        metric = balanced_accuracy_score(y, y_pred)
        print('El valor de Accuracy en {} es de: {}'.format(stage, metric))
        return metric
    
    train_metric = _callback(model, preprocess, X_train, y_train, 'Train')
    test_metric = _callback(model, preprocess, X_test, y_test, 'Train')
    return train_metric, test_metric