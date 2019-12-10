    file dispenser dispenses files
    
    for each file:
        header extractor tries to extract a meaningful header from file
            
        if that doesn't succeed:
            header generator creates a generic header instead
                
        PDF concatenator concatenates the file together with the resulting
        header
        
    PDF concatenator writes the resulting file to disk