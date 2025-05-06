More detailed information about the use of RCTab is available here to complement the [**Quick Start User Guide**](user_guide.md).


# Output Files
More information about RCTab output files.  

## Detailed Report
Detailed information about the `detailed_report`.

# Running RCTab
Some extended information about running RCTab within the context of its computer hardware and operating system. 

## RCTab and Memory Usage 
RCTab is developed knowing that different jurisdictions have different resources to devote to the machine that RCTab is run on.
RCTab can be run on most commercial, off-the-shelf hardware (COTS). 
RCTab can be run on a cutting edge, well-resourced computer (preferred) but also can be run on dusty old machines that might not be as powerful.
RCTab is thoroughly tested on hardware with different resources allocated. Use the following baselines to set expectations for your set-up.

**4GB RAM**
Should expect this

## Increasing memory allocated for RCTab
For large contests, RCTab can be told explicitly to use more resources on the computer.
This can speed up tabulation for large contests. Here is how to do that.  


1. Determine how much memory your computer has. On Windows Press Ctrl + Shift + Esc to open Task Manager. Click on the Performance tab. Click Memory on the left. You'll see "Total Installed RAM." 
2. Determine how much to allocate explicitly for RCTab. Use ~80% of your total RAM. Step in chunks of 512MB. So for 16GB use 12,800MB. `.8 * (16*1024)` rounded to the nearest 512 = `12,800`  
3. Open a Command Prompt and navigate to the `rcv` folder where RCTab was installed or unzipped.
4. Launch the tabulator by entering the following command: `.\bin\java -mx12800m -p .\app -m network.brightspots.rcv/network.brightspots.rcv.Main`