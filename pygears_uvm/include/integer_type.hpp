#ifndef INTEGER_TYPE_HPP_
#define INTEGER_TYPE_HPP_

#include <iostream>
#include <sstream>
#include <string>
#include <systemc>

template <class dt> class integer_type {
public:
  dt data;

  integer_type() : data(0) {}
  integer_type(unsigned int d) : data(d) {}
  integer_type(int d) : data(d) {}

  void operator=(const unsigned int rhs) { data = rhs; }
  void operator=(const int rhs) { data = rhs; }
  void operator=(const integer_type rhs) { data = rhs.data; }

  template<int W>
  void operator=(const sc_dt::sc_uint<W> rhs) {
    data = (dt)rhs;
  }
  template<int W>
  void operator=(const sc_dt::sc_int<W> rhs) {
    data = (dt)rhs;
  }

  void set(const dt data_rhs) const { data = data_rhs; }

  bool eos() const { return false; }

  unsigned int pack() const { return (unsigned int)data; }

  operator unsigned int() const { return (unsigned int)data; };

  operator int() const { return (int)data; };

  template <class D>
  friend std::ostream &operator<<(std::ostream &out, const integer_type<D> &q);

  std::string str() {
    std::stringstream ss;
    ss << "0x" << std::hex << data;
    return ss.str();
  }
};

template <class D>
std::ostream &operator<<(std::ostream &out, const integer_type<D> &q) {
  out << "Data: " << q.data << std::endl;
  return out;
}

#endif
