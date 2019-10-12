#include <iostream>
#include "scoreboard.hpp"
#include <systemc>
#include <sstream>

std::ostringstream display_cmp(double ref, double dut){
  std::ostringstream str;
  str << "expected : " << ref << " received: " << dut;
  return str;
}

void scoreboard::check(){
  std::deque<std::deque<unsigned int > > ref_ii;
  ref_ii.emplace_back();

  sc_core::sc_spawn_options opts;
  sc_spawn([&]() {
             int y = 0;
             int x = 0;
             while(true){
               sc_core::wait(dout_e);

               if(dout_data.front().size() == 0){
                 dout_data.pop_front();
                 y++;
                 x = 0;
               }
               unsigned int dut = dout_data.front().front();
               dout_data.front().pop_front();
               auto ref = ref_ii.at(y).at(x);
               x++;

               if(ref != dut){
                 UVM_INFO("MISMATCH", display_cmp(ref, dut).str() , uvm::UVM_LOW);
               }
               else{
                 UVM_INFO("MATCH", display_cmp(ref, dut).str() , uvm::UVM_LOW);
               }
             }
           }, "checker_thread", &opts);

  int sum_row = 0;
  int y = 0;
  int x = 0;
  while(true){
    sc_core::wait(din_e);

    if(din_data.front().size() == 0){
      y++;
      x = 0;
      sum_row = 0;
      din_data.pop_front();
      ref_ii.emplace_back();
    }
    sum_row += din_data.front().front();
    din_data.front().pop_front();

    if(y > 0){
      ref_ii.back().push_back(sum_row + ref_ii.at(y-1).at(x));
    }
    else
      ref_ii.back().push_back(sum_row);

    x++;

  }
}
