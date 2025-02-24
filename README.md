# os-scheduling-algorithms
In this lab you and your partner will implement two of the process scheduling algorithms using Python.

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create –name os-scheduling-alg python=3.13.1</li>
		<li>conda activate os-scheduling-alg</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the prod_cons_buff anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
  <li>Select a scheduling algorithm</li>
  <ul><li>You and your partner will select one algorithm. Based on your selection, I will assign you a seccond algorithm to implement. Your implementation should include the following classes.</li></ul>
  <li>Process Class</li>
  <ul><li>This class will contain any necessary attributes needed to describe a process so the scheduler can schedule the process appropriately.</li>
  <li>__str__: You will need to implement the str method that determines how a process will be represented as a string.</li>
  <li>__lr__: You will need to implement the lt method that determines how processes are compared.</li></ul>
  <li>CustomQueue Class</li>
  <ul><li>You will need to implement a CustomQueue class to represents the ready queue of processes that have been scheduled and ready to run based on the algorithm in use.</li>
  <li>Include any attributes needed to describe the queue that are needed for scheduling.</li>
  <li>put method: Implement the put method that adds a process to the queue</li>
  <li>get method: Implement the get method that returns the appropriate process from the queue</li>
  <li>__lt__: Some algorithms may need to compare queues. You will need to implement the lt method to determine how to compare queues.</li></ul>
  <li>CustomScheduler Class</li>
  <ul><li>The custom scheduler represents the scheduler that will schedule processes to the ready queue and consume processes from the ready queue according to the algorithm.</li>
  <li>schedule method: Implement the schedule method that assigns processes to the ready queue.</li>
  <li>consume method: Implement the consume method to mimic the scheduler selecting the correct next process to exectute from the ready queue. </li></ul>
  <li>Other: You may include other helper methods as needed.</li>
  <li>Demonstrate Scheduling</li>
  <ul><li>Your code should also demonstrate the scheduling algorithm in action. I should be able to run your code and processes should be placed and removed from the queue according to the algorithm. This means you should create any necessary queues, processes and call any necessary functions or methods.</li></ul>
</ol>

