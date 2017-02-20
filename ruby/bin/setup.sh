#!/usr/bin/env bash
yum install -y ruby ruby-devel
yum install -y gcc
gem install selenium-webdriver
gem install headless
yum install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz -O /tmp/geckodriver-v0.14.0-linux64.tar.gz && tar zxvf /tmp/geckodriver-v0.14.0-linux64.tar.gz -C /bin/
yum install Xvfb