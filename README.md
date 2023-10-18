# Team_M_15_Project

2023.10.18:(Written By Na Siyu)

- Already connect with the database, now all of the data come from db

- Now wait for user and manager's pages to connect, I have to mention that, they must have functions like:
- - User:
- - - 1.should have rent and return, which means change the is_use into user_id in **Table Bike**, and create or update an Order in **Table Order**
- - - 2.can see his or her orders
- - - 3.can see his or her reports

- - Manager:
- - - 1.can see All Users
- - - 2.can see All Operator
- - - 3.can delete or create a bike
- - - 4.can vitualize the data(quit hard)

- now Map Function is important for us now

- also, I create a **bike_info**, which is a little page for bike, When user click into it, it will have "Rent" and "Return", but opertor will have "Fix" or "Charge", while "Manager" will have "delete", they share the same one
- Any **frame** questions are permitted, you can just copy my **opertor_view** to create your own manager page
- Nevermind I have miswrited the "operator" to "opertor"......:(

_ **important**
- now accounts are like this, use email and password to login(now we only have operator page so only this one can be opened)
- User Tom: 123@qq.com 123456
- Operator GlasgowOperator: Glasgow@qq.com 123456
- Manager admin: admin@qq.com 123456
- **Now the password has been hashed**