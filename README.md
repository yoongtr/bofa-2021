# React Typescript App for GTT Check - BofA Code to Connect 2021
Tran Thuy Dung

## Install dependencies
* Using conda enviroment
```.bash
conda create --name <env> --file requirements.txt
pip install uvicorn
pip install fastapi
```
* Start frontend (default port is 3000)
```.bash
npm install
npm start
```
* React app is running at http://localhost:3000
* Start backend data processor
```.bash
uvicorn gtt_check:api --reload --port 8000
```
