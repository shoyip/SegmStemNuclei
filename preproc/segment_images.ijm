input = getDirectory("Choose Source Dir of Images");
list = getFileList(input);
input_tagged = getDirectory("Choose where to move tagged images");
output = getDirectory("Choose Destination Dir of Images");

for (i=0; i<list.length; i++)
	// call the ImageSegment function defined below
	ImageSegment(input, list[i], i);

function ImageSegment (input, filename, index) {
	// open the desired file
	open(input + filename);
	
	// run the Regions of Interest Manager
	run("ROI Manager...");
	roiManager("Show All");

	// set Freehand selection
	setTool("freehand");

	// wait for user to select nuclear areas
	// user can then choose to add another nucleus
	// by using the "Add" button in the ROI Manager
	waitForUser("Select nuclei");

	// how many ROIs are there?
	count = roiManager("count");

	// combine the selected ROIs into one selection
	if (count>1) {
		// select all ROIs
		selectAllROIs();

		roiManager("Combine");
	}

	// create mask and save
	run("Create Mask");
	selectWindow("Mask");
	saveAs("tiff", output+filename);
	close("*");

	// move the file to the folder of already tagged images
	File.rename(input + filename, input_tagged + filename);

	// close ROI manager
	selectWindow("ROI Manager");
	run("Close");
}

function selectAllROIs () {
	count = roiManager("count");

	array = newArray(count);
	for (i=0; i<array.length; i++) {
		array[i] = i;
	}

	roiManager("select", array);
}
