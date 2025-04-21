import sqlite3  # Assuming the database is SQLite; adjust for your database type
import json

def faster_rcnn_to_yolo(x_min, y_min, x_max, y_max, img_width, img_height):
    """
    Convert Faster R-CNN bounding box coordinates to YOLO format.
    Args:
        x_min, y_min, x_max, y_max: Bounding box coordinates from Faster R-CNN.
        img_width, img_height: Dimensions of the image.
    Returns:
        YOLO format coordinates: (x_center, y_center, width, height)
    """
    x_center = (x_min + x_max) / 2 / img_width
    y_center = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height
    return x_center, y_center, width, height

def fetch_data_from_db(db_path):
    """
    Fetch bounding box data and image dimensions from the database.
    Args:
        db_path: Path to the SQLite database.
    Returns:
        List of tuples containing bounding box data and image dimensions.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Adjust the query based on your database schema
    query = """
    SELECT x_min, y_min, x_max, y_max, img_width, img_height 
    FROM bounding_boxes
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def main():
    db_path = "path_to_your_database.db"  # Replace with your database path
    output_file = "yolo_coordinates.json"  # Output file to save YOLO coordinates

    # Fetch data from the database
    data = fetch_data_from_db(db_path)

    yolo_coordinates = []
    for record in data:
        x_min, y_min, x_max, y_max, img_width, img_height = record
        yolo_coord = faster_rcnn_to_yolo(x_min, y_min, x_max, y_max, img_width, img_height)
        yolo_coordinates.append(yolo_coord)

    # Save YOLO coordinates to a JSON file
    with open(output_file, "w") as f:
        json.dump(yolo_coordinates, f, indent=4)

    print(f"YOLO coordinates saved to {output_file}")

if __name__ == "__main__":
    main()