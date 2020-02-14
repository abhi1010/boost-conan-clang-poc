
#include <cstdlib>
#include <iostream>
#include <string>

#include <boost/foreach.hpp>

int main() {
  std::string hello("Hello, world!");

  BOOST_FOREACH (char ch, hello) { std::cout << ch; }

  return 0;
}
