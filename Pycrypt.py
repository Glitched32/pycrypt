class encoder:
    def numbers_encoder(Numbers):
        import random
        output=Numbers
        from count import number_counter
        range_finder = number_counter(Numbers)
        Key_rand = random.randrange(1, 1000)
        for i in range(range_finder):
            output = output*Key_rand
        nkey = range_finder
        okey = Key_rand
        return output, okey, nkey
class decoder:        
    def numbers_decoder(encrypted_number, okey, nkey):
        for i in range(nkey):
            output= encrypted_number/okey
            encrypted_number=output
        int(output)
        return output



        
            
        
        
    
    