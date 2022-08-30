# this is the file where you can configure the program's parameters, such as:
# amount of trains recorded each call,
# stopID,
# output type (though not recommended)

# URL Fields
# These include things such as the stopID, output type, and amount of trains.

# stopID is the stop that the API is checking. The default is 30050, the inner loop platform at State/Lake.
stopID = 30050

# amt is the amount of trains we want to display each call. The data is displayed in order of scheduled arrival times.
# The default is 5.
amt = 5

# output type changes the type of output. While we could do either JSON or XML, XML currently isn't supported.
# currently it is only included in case I add XML support later. The default is JSON.
outputType = "JSON"




