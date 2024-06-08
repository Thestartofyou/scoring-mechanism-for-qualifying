import json
from datetime import datetime

# Project data as a dictionary
project_data = {
    "project_information": {
        "project_type": "Residential units",
        "total_unit_count": 46,
        "awarded": True,
        "price_type": "Real price",
        "owner": "Not specified",
        "areas_included": "All specified scopes outlined in the drawings, spec book, and scope sheet from DBJKS",
        "specs_to_follow": "Conformed Plans and Specifications, Transmittal and change logs since CD set",
        "scope_document": True
    },
    "cabinets": {
        "construction_spec": "Not specified",
        "finish_specs": "Not specified",
        "door_style_spec": "Not specified",
        "product_decision": "Not specified"
    },
    "closets": {
        "pricing_opportunity_discussed": "Not specified",
        "spec_details": "Not specified"
    },
    "countertops": {
        "material_brand_color_thickness": "Not specified",
        "backsplash": "Not specified",
        "ve_options": "Not specified",
        "edge_profile": "Not specified",
        "sink_spec": "Not specified",
        "pricing_details": "Not specified",
        "special_requests": "Not specified"
    },
    "amenities": {
        "must_price_amenities": "Not specified",
        "amenity_locations": "Not specified",
        "amenity_material_finish": "Not specified"
    },
    "final_decision_to_bid": {
        "expected_first_delivery_date": "Not specified",
        "preferred_vendor": "Not specified",
        "contact_person": "Not specified",
        "estimator_message": "Not specified",
        "email_linked": "Not specified",
        "lead_decision": "Not specified"
    },
    "metadata": {
        "document_date": str(datetime.now())
    }
}

# Save data to a JSON file
with open('project_data.json', 'w') as f:
    json.dump(project_data, f, indent=4)

def calculate_score(data):
    score = 0
    max_score = 100  # Total maximum score
    
    # Define score weights for each field
    weights = {
        "project_information": {
            "project_type": 1.5,
            "total_unit_count": 1.5,
            "awarded": 1.5,
            "price_type": 1.5,
            "owner": 1,
            "areas_included": 1.5,
            "specs_to_follow": 1.5,
            "scope_document": 1.5
        },
        "cabinets": {
            "construction_spec": 2.5,
            "finish_specs": 2.5,
            "door_style_spec": 2.5,
            "product_decision": 2.5
        },
        "closets": {
            "pricing_opportunity_discussed": 5,
            "spec_details": 5
        },
        "countertops": {
            "material_brand_color_thickness": 1.4,
            "backsplash": 1.4,
            "ve_options": 1.4,
            "edge_profile": 1.4,
            "sink_spec": 1.4,
            "pricing_details": 1.4,
            "special_requests": 1.4
        },
        "amenities": {
            "must_price_amenities": 3.3,
            "amenity_locations": 3.3,
            "amenity_material_finish": 3.3
        },
        "final_decision_to_bid": {
            "expected_first_delivery_date": 1.66,
            "preferred_vendor": 1.66,
            "contact_person": 1.66,
            "estimator_message": 1.66,
            "email_linked": 1.66,
            "lead_decision": 1.66
        }
    }

    for category, fields in weights.items():
        for field, weight in fields.items():
            if data[category].get(field, "Not specified") != "Not specified":
                score += weight

    return score, max_score

def generate_report(data):
    score, max_score = calculate_score(data)
    report = []
    report.append("Project Information:")
    report.append(f"  Project Type: {data['project_information']['project_type']}")
    report.append(f"  Total Unit Count: {data['project_information']['total_unit_count']}")
    report.append(f"  Awarded: {'Yes' if data['project_information']['awarded'] else 'No'}")
    report.append(f"  Price Type: {data['project_information']['price_type']}")
    report.append(f"  Owner: {data['project_information']['owner']}")
    report.append(f"  Areas Included: {data['project_information']['areas_included']}")
    report.append(f"  Specs to Follow: {data['project_information']['specs_to_follow']}")
    report.append(f"  Scope Document: {'Yes' if data['project_information']['scope_document'] else 'No'}")
    report.append("\nCabinets:")
    report.append(f"  Construction Spec: {data['cabinets']['construction_spec']}")
    report.append(f"  Finish Specs: {data['cabinets']['finish_specs']}")
    report.append(f"  Door Style Spec: {data['cabinets']['door_style_spec']}")
    report.append(f"  Product Decision: {data['cabinets']['product_decision']}")
    report.append("\nClosets:")
    report.append(f"  Pricing Opportunity Discussed: {data['closets']['pricing_opportunity_discussed']}")
    report.append(f"  Spec Details: {data['closets']['spec_details']}")
    report.append("\nCountertops:")
    report.append(f"  Material Brand and Color Specs: {data['countertops']['material_brand_color_thickness']}")
    report.append(f"  Backsplash: {data['countertops']['backsplash']}")
    report.append(f"  VE Options: {data['countertops']['ve_options']}")
    report.append(f"  Edge Profile: {data['countertops']['edge_profile']}")
    report.append(f"  Sink Spec: {data['countertops']['sink_spec']}")
    report.append(f"  Pricing Details: {data['countertops']['pricing_details']}")
    report.append(f"  Special Requests: {data['countertops']['special_requests']}")
    report.append("\nAmenities:")
    report.append(f"  Must Price Amenities: {data['amenities']['must_price_amenities']}")
    report.append(f"  Amenity Locations: {data['amenities']['amenity_locations']}")
    report.append(f"  Amenity Material and Finish: {data['amenities']['amenity_material_finish']}")
    report.append("\nFinal Decision to Bid:")
    report.append(f"  Expected First Delivery Date: {data['final_decision_to_bid']['expected_first_delivery_date']}")
    report.append(f"  Preferred Vendor: {data['final_decision_to_bid']['preferred_vendor']}")
    report.append(f"  Contact Person: {data['final_decision_to_bid']['contact_person']}")
    report.append(f"  Estimator Message: {data['final_decision_to_bid']['estimator_message']}")
    report.append(f"  Email Linked: {data['final_decision_to_bid']['email_linked']}")
    report.append(f"  Lead Decision: {data['final_decision_to_bid']['lead_decision']}")
    report.append(f"\nScore: {score}/{max_score}")
    report.append(f"Report generated on: {data['metadata']['document_date']}")

    return "\n".join(report)

# Load data from JSON file
with open('project_data.json', 'r') as f:
    loaded_data = json.load(f)

# Generate and print the report
report = generate_report(loaded_data)
print(report)

# Save the report to a text file
with open('project_report.txt', 'w') as f:
    f.write(report)
