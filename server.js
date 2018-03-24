const password = require("./get_password");
const haversine = require('haversine');
const express = require('express');
var bodyParser = require('body-parser');

const app = express()
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : password.get_password(),
  database : 'trash'
});

connection.connect();

app.get('/user/:id', (req, res) => {
	let id = req.params.id;
	// SANITIZE THIS.
	connection.query("SELECT * FROM USERS WHERE id=" + id, function(error, results, fields) {
		if (error) {
			res.send({
				"error": error
			});
		}
		else {
			res.send(results);
		}
	});
});

app.get('/all_users', (req, res) => {
  connection.query("SELECT * FROM USERS", function(error, results, field) {
    if(error) {
      res.send({
        "error": error
      });
    }
    else {
      res.send(results);
    }
  });
});

app.get('/bin/:id', (req, res) => {
  let id = req.params.id;

  connection.query("SELECT * FROM BINS WHERE id=" + id, function(error, results, fields) {
    if (error) {
      res.send({
        "error": error
      });
    }
    else {
      res.send(results);
    }
  });
});

app.get('/all_bins', (req, res) => {
  connection.query("SELECT * FROM BINS", function(error, results, field) {
    if(error) {
      res.send({
        "error": error
      });
    }
    else {
      res.send(results);
    }
  });
});

app.get('/promotion/:id', (req, res) => {
  let id = req.params.id;

  connection.query("SELECT * FROM PROMOTIONS WHERE id=" + id, function(error, results, fields) {
    if (error) {
      res.send({
        "error": error
      });
    }
    else {
      res.send(results);
    }
  });
});

app.get('/all_promotions', (req, res) => {
  connection.query("SELECT * FROM PROMOTIONS", function(error, results, field) {
    if(error) {
      res.send({
        "error": error
      });
    }
    else {
      res.send(results);
    }
  });
});

app.post('/nearest_bin', function(req, res) {
  var start = {
    latitude: req.body.lat,
    longitude: req.body.lon
  };
  console.log(start);

  connection.query("SELECT * FROM BINS", function(error, results, field) {
    if(error) {
      res.send({
        "error": error
      });
    }
    else {
      console.log("Hello!");
      var min_distance_index;
      var min_distance;
      console.log("Results.length = " + results.length);
      for(i=0; i < results.length; i++) {
        console.log(i);
        var end = {
          latitude: results[i].lat,
          longitude: results[i].lon
        }
        distance = haversine(start, end);
        if(i==0){
          min_distance_index = 0;
          min_distance = distance;
        }
        else {
          if(distance < min_distance) {
            min_distance = distance;
            min_distance_index = i;
          }
        }
      }
      res.send(results[min_distance_index]);
    }
  });
});

app.listen(5000, () => console.log('Example app listening on port 5000!'))
