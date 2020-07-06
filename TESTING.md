"COVID-19 App"
Puyuan Zhang, Neal Kornreich, Surya Jagannadh Jatavallabhula, Jonathan Prindle

Test 1:

Case Name: Routes (automated test case)
Description: 
Test if the routes are routing to the proper page.

Pre-Conditions:
N/A, everything should be set up for the test.

Test steps: 
1) Run flask web app.
2) Run the flask_main.test.py script.
3) Verify results

Expected results:
User should be able to run the test to see if the test route is populating with the proper content.

Actual results:
User is able to run test and see if the route is connecting to the proper content.

Status:
Pass

Notes:
N/A

Post-conditions:
Routes appear to be functioning properly.

Test 2:
Case Name: Invalid Routes (automated test)

Description:
If the user inputs an improper name for the site, they should be redirected to a different error message as specified by the admin of the website.

Pre-conditions:
Enter in an invalid route while on the web app.

Test Steps:
1) Run flask with the web app.
2) Enter in an invalid route.
3) Verify the error/redirect message.

Expected results:
User should be redirected to a admin specified error message.

Actual results:
User is redirected to an admin specific error message.

Status:
Pass

Notes:
N/A

Post-conditions:
Users are redirected properly if they end up entering an invalid address.

Test 3:
