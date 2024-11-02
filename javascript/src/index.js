const express = require("express");
require("dotenv").config();

const cors = require("cors");
const mongoose = require("mongoose");

mongoose
  .connect(process.env.MDB_DATA)
  .then(() => console.log("Conectado a MongoDB"))
  .catch((err) => console.error("Error conectando a MongoDB", err));
