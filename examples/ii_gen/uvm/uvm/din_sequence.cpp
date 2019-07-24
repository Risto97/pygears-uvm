#include "din_sequence.hpp"

using din_sequence_packet = dti_packet<queue_type<sc_dt::sc_uint<8>, 2>>;
template class din_sequence<din_sequence_packet, din_sequence_packet>;

template <typename packet_type, typename RSP>
void din_sequence<packet_type, RSP>::gen_seq() {
  for (int j = 0; j < 5; j++) {
    std::vector<unsigned int> lower;
    for (int i = 0; i < 5; i++) {
      lower.push_back(i + 1);
    }
    data.push_back(lower);
  }
}
