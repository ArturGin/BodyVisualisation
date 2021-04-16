// Q: How to show bodies and what does it mean to see a group of dead people?

To answer this question I decided to use: --Django(as I know it), --PostgreSQL database(which I saw used a lot) --React(as it seems really exciting) --Somekind of 3D library(three js or P5js or maybe zdog?)

///Backend: Super easy.

---REST API Django framework, -import_export library for getting the database (Very nice and easy to use throught admin) -A database with needed info from https://public.emdat.be/ (awesome website) /Note for future self/ Had to trim the database down to need columns which is not epic. Maybe a better way working with models and DB? A python script which helps you do that? -Plip plop connect some dots. Instal and use import_export module and import the db. -Serialize acquired data into JSON, set up the correct views to urls and we are off to the races.

/// A few words to clarify my choices and outline further study about DB, SPA/API division, use of JSON(serialization and parsing)

DB. I did not choose the DB throught personal preference rather based on amount times I saw a certain SQL db mentioned in job offers. Gotta work on that!

SPA/API division. That just sounded so god damn cool when I hearded on my cousin's hackathon. That his company has an API which they use to connect to their app, to their website and to a Telegram Bot. So far I can see how usefull this style fo design is and how diffucult it is (smooooth transition to the next point)

-JSON serialization and parsing. Has to be a good structure/design philosophy used to send and parse JSON. As so far as I am doing it, it is very cluncky.

///Frontend

---React -Truly delightful to use and to separate everything into their own separate little packages. Good stuff. -Have not even started to deal with CSS, external frameworks(bootstrap etc.) to style and to flex my desing muscle

---3D Libraries -Now we slowly arriving at present moment. My computer sucks and combing 3D libraries with React also kinda suck. So it is not only agonisingly slow but it is also hard to combine with React which I want to use.

... From here new updates ...