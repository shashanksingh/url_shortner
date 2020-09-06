# URL Shortner Service
• As a user I want to create a new shortened URL
• As a user I want to view the details of a shortened URL
• As a user I want to see all shortened URLs that have been created
• As a user I want my shortened URL to redirect to the original URL

# Features
1. Can create short URl for long URL
2. Using API can show all short url that exists
3. Can get details for a short url
4. if already exits dont create new, send old one 
5. Test : E2E test on controller using test container , GRPC is comes with self test so no need to test that.
6. 


Todo :
1. Get everything running with docker compose
2. generate a UI ?????
3. Caching ???

# INSTALLATION
Please read SETUP.md file


# Architecture
1. Microservices talk to each other through GRPC / Proto 3
2. Separation of concern is implemented on service level
3. Docker compose is used to create architecture


# Future to handle load if it increase to Millions req/second
1. Use GRPC Web Proxy to automatically generate json api from proto descriptions. https://github.com/grpc/grpc-web with
Enovy as reverse proxy
2. Cacheing Using Redis
3. Production/Dev split
4. connect to config server and save config in consul
5. Sharding on mysql database or Move to Nosql like Cassandra 
6. Use ""wait for service to use docker compsoe for full architecture generation
7. Use Alembic to generate schema instead of hardcoded one in case of 

# DB performance
Do load tests autogenerated result

-------------------------------------------- benchmark: 1 tests --------------------------------------------
Name (time in ms)        Min     Max    Mean  StdDev  Median     IQR  Outliers       OPS  Rounds  Iterations
------------------------------------------------------------------------------------------------------------
test_performance      1.5208  8.3256  4.0971  2.2813  5.4996  4.2660      14;0  244.0771      29           1
------------------------------------------------------------------------------------------------------------

Legend: 
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean



