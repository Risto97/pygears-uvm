#ifndef DIN_SEQUENCE_CG_HPP_
#define DIN_SEQUENCE_CG_HPP_

#include "scoreboard.hpp"
#include <cmath>
#include <iostream>

#define DIN_SEQUENCE_CGROUPS DIN_CGROUP din_cg;

class DIN_CGROUP : public covergroup{
public:

  unsigned int din = 0;

  CG_CONS(DIN_CGROUP) {
  }

  void sample(unsigned int value) {
    this->din = value;
    covergroup::sample();
  }

  COVERPOINT(unsigned int, din_cvp, din) {
    bin<unsigned int>("ZERO", 0),
      bin<unsigned int>("rest", interval(1,254)),
      bin<unsigned int>("MAX", 255)
      };

};

#endif
