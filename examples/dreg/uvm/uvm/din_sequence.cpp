#include "din_sequence.hpp"

using din_sequence_packet = dti_packet<queue_type<sc_dt::sc_uint<8>, 2>>;
template class din_sequence<din_sequence_packet, din_sequence_packet>;

template <typename packet_type, typename RSP>
void din_sequence<packet_type, RSP>::gen_seq() {}