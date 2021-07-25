# E-Commerce website
Simple E-Commerce website

#### Run instruction

Install all packages
```
pip install -r requirements.txt
```

Run the server
```
python server.py
```
In other Terminal
```
python to_database.py
```
```
Open About.html
```
Server runs at
```
http://localhost:5000/
```

#### Routes

Products
```python
GET Request
URL = 'http://localhost:5000/products'
params = {}

Response
[
    {
        "image": "http://res.cloudinary.com/dnhwxgf8i/image/upload/c_scale,h_250,w_400/v1488011915/mockup3_kxxwfy.jpg", 
        "category": "Tables", 
        "item": "Pearl Galaxy", 
        "price": "$2,100"
    }, 
    {
        "image": "http://res.cloudinary.com/dnhwxgf8i/image/upload/c_scale,h_250,w_400/v1488011915/mockup1_ff4smb.jpg", 
        ...
    }
]
```
