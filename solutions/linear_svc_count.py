count_svc = LinearSVC()
count_svc.fit(count_train, y_train)
pred = count_svc.predict(count_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)
cm = metrics.confusion_matrix(y_test, pred, labels=[trump.name, trudeau.name])
plot_confusion_matrix(cm, classes=[trump.name, trudeau.name])
