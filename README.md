<p align="center">
<img src="https://tctechcrunch2011.files.wordpress.com/2015/11/holberton-logo-horizontal.jpg" width="450" height="250">	
<h1> AirBnB clone - The console</h1></p>

<h3> 📝 Description</h3>
<p>This is our first step towards building our  first full web application: the AirBnB clone. This first step is very important because we will use what we built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration….
This AirBnB clone project works with a console that uses the cmd python module. This project was built with OOP so you can create, show, all, update, destroy BaseModels, places or Cities objects among others.</p>

<p align="center">
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T024230Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=90f3650d835cb98170448976664e15449232319578941bb5b395e8ddae106317" width="550" height="450"></p>

<h3> ⭐️ Installation</h3>

<p> To get usage of the console use the following command

```
git clone https://github.com/valen2510/AirBnB_clone.git
```

<h3> 🚀 Usage</h3>

<p> The Console shows a prompt and wait for the BaseModel to type a command, interpretes and run the input command and display the prompt again. You can exit the console using quit command EOF or Ctrl + D.

<h4>Interactive mode</h4>

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

<h4>Non-Interactive mode</h4>

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

<h2> ✨ Classes to build your objects</h2>

 Class name        | Attributes |
| ----------- | ----------- |
|BaseModel   | id, created_at, updated_at.|
|BaseModel   | email, password, first_name, last_name.|
|State   | name, state_id.|
|City    | name. |
|Amenity   | name.|
|Place   | city_id, BaseModel_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night latitude, longitude amenity_ids.|
|Review   | place_id, BaseModel_id, text.|

<h2> ✨ Console Commands</h2>

 Command        | Description |
| ----------- | ----------- |
|create [Class name]  | Creates a new instance of one of the classes above, saves it into a JSON file, and prints the id of the instance you created. Ex: `$ create BaseModel`.|
|show [Class name] [id]  | Prints the string representation of the instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234`.|
|destroy [Class name] [id]  | Deletes the instance based on the class name and id. Also, saves the changes into the JSON file Ex: `$ destroy BaseModel 1234-1234-1234`.|
|all [optional Class name]  | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel or $ all`.|
|update [Class name] [id] [attribute name] ["attribute value"]  | Updates an instance based on the class name and id by adding or updating attribute, saves the changes into the JSON file. Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`. |



<h3> ✍ Examples</h3>

<p> 

<h4>create command</h4>

```
(hbnh) create BaseModel
11c736fd-9638-4124-b034-632059325fa4
(hbnh)
------------------------------------
$ echo "create BaseModel" | ./console.py
(hbnb)
11c736fd-9638-4124-b034-632059325fa4
(hbnb)
$

```

<h4>show command</h4>

```
(hbnh) show BaseModel 11c736fd-9638-4124-b034-632059325fa4
[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}
(hbnb)
------------------------------------
$ echo "show BaseModel 11c736fd-9638-4124-b034-632059325fa4" | ./console.py
(hbnb)
[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}
(hbnb)
$

```

<h4>all command</h4>

```
(hbnh) all
["[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}"]
(hbnh)
------------------------------------
$ echo "all" | ./console.py
(hbnb)
["[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}"]
(hbnb)
$

```

<h4>update command</h4>

```
(hbnh) update BaseModel 11c736fd-9638-4124-b034-632059325fa4 name "Betty"
(hbnh)
------------------------------------
$ echo "update BaseModel 11c736fd-9638-4124-b034-632059325fa4 name "Betty"" | ./console.py
(hbnb)
(hbnb)
$

```

<h4>destroy command</h4>

```bash
(hbnh) destroy BaseModel 11c736fd-9638-4124-b034-632059325fa4
(hbnh)
------------------------------------
$ echo "destroy BaseModel 11c736fd-9638-4124-b034-632059325fa4" | ./console.py
(hbnb)
(hbnb)
$

```

</p>

<h3> 🤝 Contributors</h3>

<a href="https://github.com/attamakevin" target="_blank">
        <img src="https://avatars3.githubusercontent.com/u/65981858?s=460&u=917bf8544c11bfc83b5a9fd961fc72ef25e3188a&v=4" style="float: center; margin-right: 10px" height="65" width="65">
</a>
<a href="https://github.com/stellargodwin" target="_blank">
        <img src="https://avatars2.githubusercontent.com/u/60383826?s=400&u=2c0d5b6ad73dd12f883d6893f95dc9efc6f34f74&v=4" style="float: center; margin-right: 10px" height="65" width="65">
</a>

---

<br>
<p align="center">
<b>Kevin Ejike  - Stella<b><br>
</p>
<p align="center">
<b>March, 2023.<b>
</p>
