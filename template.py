actions:

loadstore upon miss:
    create_load_entry;
    request_load.

l2cache upon loadstore::load_request do:
    if load_entry_available do 
        l2cache::accept_request
        entry = l2cache::create_load_entry
        entry::send_load_request_to_bus
        entry::wait_bus_reply


l2cache::[create_load -> send_request -> wait_response -> data_arrival]

l2cache upon data_arrival call loadstore::receive_data
loadstore::[receive_data -> remove]