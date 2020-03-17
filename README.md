# Malar-Ai
Malar-ai is a handy device(based on smartphones) used to detect probable malaria infection using blood smear slides. 

Powered by pre-trained ResNet-50, cell-phone microscope and a staining kit, this setup is capable of performing at an accuracy of >95%, hence highly useful in remote and inaccessible areas. 

Files- 
-Build Dataset- @Tanay The data we have is categorised into 2- Parasitised and Non- Parasitised. Your task is to use this this file to distribute the dataset as Training, Testing and Validating. So, we will have 3 folders Testing Data, Training Data and Validation Data, with subfolders as Parasitised and non-parasitised. After that, iterate a loop over this dataset to create 3 numpy arrays as Testing_images, Training_images, Validation_images [along with labels] in such a way that @Srikanth & @Rohan can import these numpy arrays from this file. Refer OS library.
Rescale the images by 255
Sample Training dataset
[[0.2,0.25,......],[Parasitised]],
[[0.23,0.26,......],[Unparasitised]]
so on


-Build Model- @Rohan Use Keras library to build a ResNet model and train+validate it [Optimizer: opt, Loss: BinaryCrossEntropy, metrics: Accuracy] in such a way that @Srikanth can test using the testing data [Using this file].

-Test_Model- @Srikanth, test the model made by @Rohan and plot the graph of training loss+accuracy vs epoch.[save it to JPG]

Initially write the code in your respective machines and then upload here after testing

Write the comments preferably after each step and while committing to this repo!

Good Luck :)
