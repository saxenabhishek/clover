## 💡 Project Description

Clover is a library management software. It interacts with Frappe's API of 4000 books. You can keep track of book issues, view all the books, Search through users, and see reports of the month.

## 📺 Preview

<div align="center">
  <img alt="Screenshot" src="docs/preview.png" />
</div>

## 📌 Prerequisites

- node.js
- pip or poetry (Check out poetry [here](https://python-poetry.org/))

## Installation 🔧

### Step One (install python dependencies)

**poetry**

```shell
$ poetry install
```

**pip**

```shell
$ pip install -r requirements.txt
```

<br/>

### Step Two (Install node dependencies)

```shell
$ cd ./client
$ npm install
```

## 🏃 Run Services

###

Step One (Build and start the frontend)

```shell
$ cd ./client
$ npm run build
$ npm run start
```

<br/>

### Step Two (Start the backend)

```shell
$ python -m clover
```

## 📚 Stack

- Frontend
  - Next
  - ReactJS
  - Node.js
  - TailWindCSS
- Backend
  - Fast API
  - MongoDB

## 📦 Inside the box

Clover is a python package built on FastAPI. It contains three sub-packages that control operations of books, users, and records, and this makes up eight backend routes.

The client folder contains the frontend, built on next js.
There are a total of 5 frontend pages that control books that are selected, checked out, returned, etc.

## 📜 License

Clover is available under the MIT license. See the LICENSE file for more info.

## 🤝 Contributing

Please read [`Contributing.md`](https://github.com/SRM-IST-KTR/template/blob/main/Contributing.md) for details on our code of conduct, and the process for submitting pull requests to us.

## ⚙️ Maintainers

| <p align="center">![Abhishek Saxena](https://github.com/saxenabhishek.png?size=128)<br>[Abhishek Saxena](https://github.com/saxena)</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------
