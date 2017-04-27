#!/bin/bash

groupadd jenkins
useradd -G jenkins builder
passwd builder!