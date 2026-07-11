local function main() 
    local startDay = tonumber(io.read():match("Dia (%S+)"))
    local sh, sm, ss = io.read():match("(%S+) : (%S+) : (%S+)")
    sh, sm, ss = tonumber(sh), tonumber(sm), tonumber(ss)
    local startTime = (startDay * 86400) + (sh * 3600) + (sm * 60) + ss
    
    local endDay = tonumber(io.read():match("Dia (%S+)"))
    local eh, em, es = io.read():match("(%S+) : (%S+) : (%S+)")
    eh, em, es = tonumber(eh), tonumber(em), tonumber(es)
    local endTime = (endDay * 86400) + (eh * 3600) + (em * 60) + es
    
    local duration = endTime - startTime
    
    print(string.format("%.0f dia(s)", math.floor(duration / 86400)))
    duration = duration % 86400
    print(string.format("%.0f hora(s)", math.floor(duration / 3600)))
    duration = duration % 3600
    print(string.format("%.0f minuto(s)", math.floor(duration / 60)))
    duration = duration % 60
    print(string.format("%.0f segundo(s)", duration))
end

main()