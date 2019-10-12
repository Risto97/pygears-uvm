#include "din_sequence.hpp"
#include <scv.h>
#include <cmath>

using din_sequence_packet = dti_packet<queue_type<sc_dt::sc_uint<8>, 2>>;
template class din_sequence<din_sequence_packet, din_sequence_packet>;

template <typename packet_type, typename RSP>
void din_sequence<packet_type, RSP>::gen_seq() {
  scv_smart_ptr<float> img_val ("img_val");
  img_val->keep_only(0, pow(2,8)-1);

  for (int j = 0; j < 25; j++) {
    std::vector<unsigned int> lower;
    for (int i = 0; i < 25; i++) {
      img_val->next();
      lower.push_back(*img_val);
      this->din_cg.sample(*img_val);
    }
    data.push_back(lower);
  }
}
