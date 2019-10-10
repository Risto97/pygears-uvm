#ifndef PHASE_SEQUENCE_CG_HPP_
#define PHASE_SEQUENCE_CG_HPP_

#include "scoreboard.hpp"
#include <cmath>
#include <iostream>

#define PHASE_SEQUENCE_CGROUPS PHASE_CGROUP phase_cg;

class PHASE_CGROUP : public covergroup{
public:

  float phase = 0;

  CG_CONS(PHASE_CGROUP) {
  }

  void sample(float value) {
    float degrees = value * (180.0/M_PI);
    this->phase = degrees;

    covergroup::sample();
  }

  COVERPOINT(float, phase_cvp, phase) {
    bin<float>("First Quadrant", interval(0,90)),
      bin<float>("Second Quadrant", interval(90,180)),
      bin<float>("Third Quadrant", interval(180,270)),
      bin<float>("Fourth Quadrant", interval(270,360))
      };

};

#endif
