Proj3.py
1. Install:
	Install opencv in Command Promopt with following command (make sure the python version is 3.x)
	conda create -n opencv numpy scipy scikit-learn matplotlib python=3
	activate opencv
	conda install -c https://conda.binstar.org/menpo opencv3
2. Preparation:
	Put all train data folders, test image and python file into the same directory
	Train data folder 01 is smile, 02 is hat, 03 is hash, 04 is heart and 05 is dollar
	Only image files should be inside the folder
	Don't switch folder numbers and the images inside, it should be exactly same with what listed above
	For example the directory of python file is F:\proj3\Proj3.py
	And the train data folders are 01(smile), 02(hat), 03(hash), 04(heart) and 05(dollar)
	So the directory of train data folder should be F:\proj3\01, F:\proj3\02, etc. and the directory of test image should be F:\proj3\03.jpg
3. Run
	i. Active opencv enviroment in Command Promopt with following command (*If the environment is not activated, the program cannot run*)
	   activate opencv
	ii. Go to the directory of our python file
	iii. Choose one file that need to be tested
	     Type python Proj3.py [test image path] to run the program
	     For example: if I want to test the third image of hat then I should type
			  python Proj3.py 03.jpg
	iv. After few seconds, it will give a result about what the image is