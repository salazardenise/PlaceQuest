"use strict";

$(document).on('click', '.list-stuff', (evt) => {
    let facilityName = $(evt.target);
    let facility_id = facilityName.data('facility_id');

    if (facilityName.find('row').length == 0) {
            var conditions = [{'name': 'Stroke'}, {'name': 'Nervous System Disorder'}, {'name': 'Brain Disease or Condition'}, {'name': 'Spinal Cord Disease or Condition'}, {'name': 'Hip or Femur Fracture'}, {'name': 'Amputation or Join Condition'}, {'name': 'Other Conditions'}]
            
            let lst = "<br style='margin-top: 1em'><span style='font-family: Roboto; font-style: normal; font-weight: bold; font-size: 12px; line-height: normal; color: #0083B0;'>Treats:</span>"
            lst += "<ul class='programsList' style='display: none'>";
            for (let i in conditions) {
                lst += `<li style='font-family: Roboto; font-style: normal; font-weight: normal; font-size: 12px; line-height: normal; color: #393939;'>${conditions[i].name}</li>`
            }
            lst += '</ul>'
            facilityName.append(lst);
            facilityName.find('ul').slideDown('slow')
            // do not allow clicking on facilityName's children
            facilityName.children().click( (e) => {e.stopPropagation()});
    } else {
        let conditions_lst = facilityName.find('row');
        // programs_lst.remove();
        conditions_lst.slideToggle('slow');
    }
});

function initMap() {
    /////////////////////////////////////////////////////////
    // DISPLAY PROGRAMS RESULTS LOCATIONS IN MAP
    $('#programs_map').fadeIn(400, () => {});

    // create map
    let map;

    // determine where to center map
    function setCenterOfMap(search_text) {
        let location = new google.maps.Geocoder();

        location.geocode({'address': search_text}, 
            function (results, status) {
                if (status === google.maps.GeocoderStatus.OK) {
                    map = new google.maps.Map(document.querySelector('#programs_map'), {
                        center: results[0].geometry.location,
                        zoom: 8
                    });
                } else {
                    let defaultLocationUS= {lat: 39, lng: -95};
                    map = new google.maps.Map(document.querySelector('#programs_map'), {
                        center: defaultLocationUS,
                        zoom: 2
                    });
                }
            }
        )
    }
    setCenterOfMap('San Francisco, CA');

    let infoWindow = new google.maps.InfoWindow({
        width: 150
    });

    // add each facility to map with marker and info window
    function addFacilityLocationByAddress(facilityName, facilityFullAddress) {
        let facilityLocation = new google.maps.Geocoder();
        let address = facilityFullAddress;
        facilityLocation.geocode(
            {'address': address, 'region': 'US'},
            function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    let facilityLatLng = results[0].geometry.location;
                    let facilityMarker = new google.maps.Marker({
                        position: facilityLatLng,
                        map: map,
                        title: facilityName,
                    }); 
                    // Define the content of the infoWindow
                    let html = (
                        '<div>' +
                        '<p>' + facilityName + '</p>' +
                        '<p>' + facilityFullAddress + '</p>' +
                        '</div>'
                    );
                    // bind an infowindow to the marker
                    google.maps.event.addListener(facilityMarker, 'click', function () {
                        infoWindow.close();
                        infoWindow.setContent(html);
                        infoWindow.open(map, facilityMarker);
                    });
                } else {
                    console.log('Geocode not successful for ' + address)
                }
            }
        )
    }

    $.get('/results.json', (results) => {
        for (let i in results) {
            let facilityFullAddress = results[i].address;
            addFacilityLocationByAddress(results[i].name, facilityFullAddress);
        }
    });

}
