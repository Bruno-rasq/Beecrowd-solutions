while true do
    local word = io.read()
    if not word then break end
    
    if #word >= 10 then 
        print("palavrao")
    else
        print("palavrinha")
    end
end