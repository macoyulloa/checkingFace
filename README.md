# checkingFace

[add] add authentication with jwt in rails API, endpoints
http://localhost:3000/api/users POST allows creating a new user
http://localhost:3000/api/users/login POST, to log a user with password and email, and returns a JWT token to retrieve the user info in JSON

http://localhost:3000/api/user, GET show a user, you must send in Authorization Header a Bearer token

http://localhost:3000/api/user, PATCH or PUT, you must send in Authorization Header a Bearer token
http://localhost:3000/api/all, GET returns all users in database, this is a public endpoint
