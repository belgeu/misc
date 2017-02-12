=begin
Webdriver test (CentOS7)

To run test:
- install ruby
    yum install ruby ruby-devel
- install gcc
    yum install gcc
- install latest Selenium version and headless
    gem install selenium-webdriver
    gem install headless
- install latest Firefox browser
    yum install firefox
- get latest geckodriver
    https://github.com/mozilla/geckodriver/releases
- install Xvfb
    yum install Xvfb

Execute:
# ruby webdriver_test.rb


GIT

mkdir /root/python/practice
cd /root/python/practice
git clone https://github.com/belgeu/misc.git
cd misc
## edit .git/config to ask pass (add belgeu@ to url)
## url = https://belgeu@github.com/belgeu/misc.git
git add webdriver_test.rb
git commit -m "Initial revision of webdriver test for Ruby"
git push origin master

DOCs:
- Selenium Finding elements
https://gist.github.com/huangzhichong/3284966



=end

require 'selenium-webdriver'
require 'headless'

def setup
  @screen = Headless.new
  @screen.start
  @b = Selenium::WebDriver.for :firefox
end

def teardown
  @b.quit
  @screen.destroy
end

def run
  setup
  yield
  teardown
end

run do
  @b.get 'https://www.ruby-lang.org/en/'
  @b.save_screenshot '/var/www/html/ruby_test.png'
  wait = Selenium::WebDriver::Wait.new(:timeout => 10)
# Search for Ruby download link
  wait.until {
    @b.find_element(:class , "download-link")
  }
  e = @b.find_element(:class, "download-link")
  e.click
# Search for Ruby 2.4.0
  wait.until {
    @b.find_element(:link_text , "Ruby 2.4.0")
  }
  
end
