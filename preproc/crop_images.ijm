input = getDirectory("Choose Source Dir of Images");
list = getFileList(input);
output = getDirectory("Choose Destination Dir of Images")

for (i=0; i<list.length; i++)
	// call the multicrop function defined below
	ImageMultiCrop(input, list[i], i);

function ImageMultiCrop (input, filename, index) {
	// open the desired file
	open(input + filename);

	// run the Regions of Interest Manager
	run("ROI Manager...");
	roiManager("Show All");

	// create Dialog box
	// actions = newArray("+", "Next");
	// Dialog.create("Add selection area");
	// Dialog.addMessage("Click on + to add area and Next to save the images and check the next ones");
	// Dialog.addRadioButtonGroup("actions", actions, 1, 2, "+");
	// Dialog.show();
	// choice = Dialog.getRadioButton();

	// set Rectangular Selection
	setTool("Rectangular");

	// wait for the user to select a rectangular area
	// user can choose to add multiple areas using the
	// "Add" button in the ROI Manager
	waitForUser("Select areas");

	// when user hits OK, crop everything and save
	RoiManager.multiCrop(output, " save tif");

	// close ROI manager
	selectWindow("ROI Manager");
	run("Close");

	close();
}
