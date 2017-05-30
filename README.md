# hr.ai.public
HR.ai

Interview Task:

The file descriptions.txt contains 5 text job descriptions. Descriptions are separated by ||||| and then a line ID:<ID>. The first line of each description provides the title in the format TITLE:<title>. The second line of each description provides meta data in the format META:<meta>.

The file queries.txt contain sets of queries made on LinkedIn by a recruiter who is searching for candidate resumes that will be great fits for each description.

The task is to build a model/algorithm that will automatically generate potential queries for ID:00005. (We recommend generating query-score pairs with the query ranging from 0.0 to 1.0 depending on appropriateness.)

For the model/algorithm you may use queries.txt and your own knowledge. 

Please complete at least one of the following tasks:

A) Generate 1) keywords and 2) skills for each of the job descriptions using some form natural language processing on the text.

B) Using (A) and/or queries.txt build a train/infer Tensorflow model that uses the queries of ID:00001-00004 to infer query-scores for ID:00005.

Note: You will not be evaluated on the quality of your resumes -- there is very little data -- but on the quality of your process and its structure. 

Keep in mind that we ultimately want this to scale, i.e., computationally fast, minimal reliance on hand engineered features, and applicable across any kind of software engineering job description. You will not be scored on how well your solution scales, so long as you describe how your production model would scale.

We have provided a python script that reads descriptions.txt into a list of dictionaries and queries.txt into a list of lists.

Requirements:
1. Approximately 3 hours.
2. Complete task A or B, or both.
3. Provide description how your model will scale, in comments, about 0.5-1.0 page of text.
4. Create a public repository with your solution.
5. Please DO NOT submit your solution to the hr.ai.public repository.


