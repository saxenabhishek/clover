#!/bin/bash

cd client
npm install
npm run build
cd ..

pip install -r requirements.txt