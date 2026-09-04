local segment_s = io.read()
local segment_p = io.read()

local function removeAllOccur(sgm_s, sgm_p)
    -- remove a primeira ocorrência se sgm_p em sgm_s
    local new_sgm_s, qnt = string.gsub(sgm_s, sgm_p, "", 1)
    if qnt > 0 then -- usa recursão para continuar a remover
        return removeAllOccur(new_sgm_s, sgm_p)
    end
    if #new_sgm_s == 0 then
        print("null value")
    else
        print(new_sgm_s)
    end
end

removeAllOccur(segment_s, segment_p)