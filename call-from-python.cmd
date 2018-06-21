REM *** Note ***
REM This is a sample of the script to be called by ART framework
REM Every folder, explored by the ART framework, may represent
REM different domains and may have different content of the script.

@FOR /L %%i in (1,1,2) DO (
	@echo ### Getting details of your company ###
	call curl -X GET --header "authorization: apikey <your-api-key>" "https://api.trinet.com/v1/manage-company/101/org-details"

	@echo ### Posting new department ###
	call curl -X POST --header "authorization: apikey <your-api-key>" --header "Content-Type: application/json" 
	-d "{
        \"deptCode\": \"280\",
        \"deptName\":\"HR\",
        \"shortDesc\":\"Human Resources\",
        \"effectiveDate\":\"01012018\"
	   }" "https://api.trinet.com/v1/manage-company/101/departments"

	@echo ### Getting company's departments nad veryfying previous operation ###
	call curl -X GET --header "authorization: apikey <your-api-key>" "https://api.trinet.com/v1/company/101/departments"

	echo --- Iteration *** %%i *** is finished ---
)