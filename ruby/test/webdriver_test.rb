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
