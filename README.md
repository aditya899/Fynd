This project is aimed to create a RESTFul API for movies something like IMDB. And a decent implementation to search for movies having 2 levels of access: admin = who can add, remove or edit movies. users = who can just view the movies.

Created the below API end points to get the required response.
1. Open http://localhost:8000 in browser
2. Get movie list at http://localhost:8000/api/imdb
3. Get single movie detail at http://localhost:8000/api/imdb/<name>

Once deployed suppose this application became very famous and started to receive a ton of traffic. Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous as well as authenticated users. Suggest an architecture to scale up this system to 5x of these specs.

We can perform the below activity/activities to scale up the API traffic.
1. Very first we need to replace the file based DB (sqlite3) to Production Level DB (MySQL/Postgres)
2. If we add caching mechanism(Redis) for handling large number of requests.
3. We will create DB replication for better accessibility for read & write operations saperately & for better accessiblity
4. We will have to set up a load balancer for scalling up the api & db servers
5. We can set throttling to limit requests by user/day