# **BCG Industrial IoTs - Powerclass Assignment**  

Welcome to the **BCG Industrial IoTs - Powerclass Assignment Repository**, a showcase of assignments and projects completed during the **Esan Coding Season 2 (2024)**. This repository highlights the integration of IoT concepts with cutting-edge tools and hardware, demonstrating practical applications in the industrial IoT domain.  

---

## **Overview**  
The repository encapsulates a journey into the world of **Industrial IoT** using the versatile **ESP32 microcontroller**, showcasing various real-world applications. With a hands-on approach, the projects integrate hardware, software tools, and sensors, emphasizing IoT's potential in automation and data-driven solutions.  

### **Key Components**  
- **Hardware:**  
  - ESP32: A powerful microcontroller with built-in Wi-Fi and Bluetooth, serving as the core of our IoT implementations.  
  - Sensors: DHT22 (Temperature & Humidity), Potentiometers, and more for data acquisition.  

- **Software & Tools:**  
  - **ThingSpeak:** For cloud-based IoT analytics and visualization.  
  - **WokWi:** An online ESP32 simulator for rapid prototyping.  
  - **MQTTexplorer:** For efficient message exchange using MQTT protocol.  
  - **Node-Red:** For creating dynamic IoT dashboards and workflows.  
  - **TinkerCAD:** For virtual circuit design and simulation.  
  - **Node.js:** Backend programming to enhance IoT interactions.  

---

## **Assignments and Labs**  

Each lab focuses on a specific IoT concept, building incrementally to develop a comprehensive understanding of IoT systems.  

### **LAB 1: Ohm’s Law**  
- **Description:** Investigated the relationship between voltage, current, and resistance using circuit simulations.  
- **Result:** Gained fundamental insights into electrical circuits.  
- **Reference File:** `2.1.3.png`  

---

### **LAB 2: LED Blinking (Digital)**  
- **Description:** Programmed the ESP32 to blink an LED using GPIO pins, demonstrating basic digital output.  
- **Result:** Developed foundational programming skills for digital control.  
- **Folder:** `2.2.5 folder`  

---

### **LAB 3: Counter Switch (Digital)**  
- **Description:** Created a counter system controlled by a physical switch, showcasing interaction between input and output.  
- **Result:** Enhanced understanding of user-controlled digital inputs.  
- **Folder:** `2.2.6 folder`  

---

### **LAB 4: Potentiometer (Analog)**  
- **Description:** Used a potentiometer to measure analog input and control output.  
- **Result:** Learned how to handle analog signals with ESP32.  
- **Folder:** `2.2.7 folder`  

---

### **LAB 5: DHT22 Temperature & Humidity Sensor (Analog)**  
- **Description:** Captured and displayed temperature and humidity readings using the DHT22 sensor.  
- **Result:** Explored sensor integration for data collection.  
- **Folder:** `2.3.2 folder`  

---

### **LAB 6: DHT22 with OLED Display**  
- **Description:** Combined the DHT22 sensor with an OLED display to showcase live sensor readings.  
- **Result:** Created a standalone monitoring system.  
- **Folder:** `2.3.3 folder`  

---

### **LAB 7: Cloud Integration**  
- **Part 1:** Published DHT22 sensor data from ESP32 to ThingSpeak.  
  - **Folder:** `2.4.5/Server`  
- **Part 2:** Published and subscribed to data using MQTTexplorer for efficient IoT communication.  
  - **Folder:** `2.4.5/Client`  

---

### **LAB 8: Node-Red Dashboard Integration**  
- **Description:** Published DHT22 sensor data to a custom Node-Red dashboard for visualization.  
- **Result:** Built a user-friendly interface for real-time monitoring.  
- **Folder:** `2.5.2`  

---

### **Mini Project: Temperature and Humidity Monitoring System**  
- **Description:** Designed a complete IoT system to monitor temperature and humidity, integrating all learned concepts.  
- **Result:** Demonstrated the end-to-end workflow of IoT data acquisition, processing, and visualization.  
- **Folder:** `2.6.1`  

---

## **Hardware Overview**  

Below is an image of the ESP32 module and its I/O layout, central to all the experiments conducted in this project:  

<img src="port.png" alt="ESP32 I/O Layout" width="400">  

---

## **Tool Overview**  

The following tools were pivotal in implementing the projects:  

<table>
<tr>
<td align="center"><img src="https://www.iqhome.org/image/cache/catalog/post/thingspeak-1200x750.png" alt="ThingSpeak Logo" width="100"><br><b>ThingSpeak</b></td>
<td align="center"><img src="https://avatars.githubusercontent.com/u/56967200?s=280&v=4" alt="WokWi Logo" width="100"><br><b>WokWi</b></td>
<td align="center"><img src="https://inside.wooster.edu/technology/wp-content/uploads/sites/83/2018/09/logo-tinkercad-256.png" alt="TinkerCAD Logo" width="100"><br><b>TinkerCAD</b></td>
<td align="center"><img src="https://nodered.org/about/resources/media/node-red-hexagon.png" alt="Node-Red Logo" width="100"><br><b>Node-Red</b></td>
<td align="center"><img src="https://cdn.freebiesupply.com/logos/large/2x/nodejs-1-logo-png-transparent.png" alt="MQTT Logo" width="100"><br><b>NodeJS</b></td>
<td align="center"><img src="https://user-images.githubusercontent.com/7721625/52227945-5280b580-28b1-11e9-804c-75a842537393.png" alt="MQTT Logo" width="100"><br><b>MQTTexplorer</b></td>
</tr>
</table>  

---

## **Key Learnings**  

1. **Sensor Integration:** Learned how to connect and collect data from various sensors like DHT22 and potentiometers.  
2. **IoT Protocols:** Explored MQTT for data communication and ThingSpeak for cloud-based analytics.  
3. **Dashboard Creation:** Built user-friendly interfaces using Node-Red.  
4. **Hardware Prototyping:** Gained hands-on experience with ESP32 for IoT applications.  

---

## **Future Improvements**  

- Expanding the project to support more sensors and actuators.  
- Implementing predictive analytics using AI for IoT data.  
- Enhancing security in IoT communication.  

---

This repository serves as a comprehensive guide to understanding and implementing IoT projects, combining hardware and software for practical and scalable solutions.