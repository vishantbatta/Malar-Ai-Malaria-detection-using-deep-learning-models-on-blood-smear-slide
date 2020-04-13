#testing part
#ploting is already done by rohan

model.evaluate_generator(generator=test_batches, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0)

'''X_Testing_images =[]
y_Testing_images =[]
for features, labels in test_batches:
    X_Testing_images.append(features)
    y_Testing_images.append(labels)

y_pred=model.predict(X_Testing_images, batch_size=50, verbose=0, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False)    

from sklearn.metrics import accuracy_score
accuracy_score(y_Testing_images,y_pred)*100'''           #finding accuracy of model
