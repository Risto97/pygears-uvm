#ifndef SCOREBOARD_CG_HPP_
#define SCOREBOARD_CG_HPP_

#include "scoreboard.hpp"

// #define SCOREBOARD_CGROUPS sb_coverage sinus_cg;

class sb_coverage : public covergroup{
public:

  int sine = 0;

  CG_CONS(sb_coverage) {
  }

  void sample(int value) {

    this->sine = value;

    covergroup::sample();
  }

  COVERPOINT(int, sinus_cvp, sine) {
    bin<int>("Positive", interval(0, INT_MAX)),
      bin<int>("Negative", interval(0, INT_MIN)),
      bin<int>("Zero", 0)
      };

};

#endif
