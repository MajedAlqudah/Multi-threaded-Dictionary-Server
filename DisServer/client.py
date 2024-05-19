import tkinter as tk
import socket
import json

def query_word():
    word = word_entry.get().strip()  # Remove leading/trailing whitespace
    if not word:
        result_text.config(fg="red")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Please enter a word.")
        return

    try:
        # Connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 8080))

        # Send request to server
        request = {"type": "query", "word": word}
        client_socket.send(json.dumps(request).encode())

        # Receive response from server
        response_data = client_socket.recv(1024).decode()
        response = json.loads(response_data)

        # Process response
        if response["status"] == "success":
            meanings = response["meanings"]
            result_text.config(fg="green")
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Meanings of '{}':\n".format(word))
            for meaning in meanings:
                result_text.insert(tk.END, "- {}\n".format(meaning))
        else:
            result_text.config(fg="red")
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error: {}\n".format(response["message"]))
    except Exception as e:
        result_text.config(fg="red")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Failed to connect to server.")
    finally:
        client_socket.close()
        word_entry.delete(0, tk.END)  # Clear input field

def clear_result():
    result_text.delete(1.0, tk.END)  # Clear result area

# Create GUI window
root = tk.Tk()
root.title("Dictionary Client")
root.geometry("600x400")

# Set background color
root.config(bg="#808080")

# Word entry
word_label = tk.Label(root, text="Enter a word:", bg="#808080",fg ='white', font=("Arial", 12))
word_label.pack(pady=10)
word_entry = tk.Entry(root, font=("Arial", 12))
word_entry.pack(ipadx=50, ipady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=query_word, bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=5, ipadx=10, ipady=5)

# Result text area
result_label = tk.Label(root, text="Meanings:", bg="#808080", fg = 'white', font=("Arial", 12))
result_label.pack(pady=10)
result_text = tk.Text(root, height=6, width=40, font=("Arial", 12))
result_text.pack()

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_result, bg="#f44336", fg="white", font=("Arial", 12))
clear_button.pack(pady=10, ipadx=10, ipady=5)


# Run the GUI
root.mainloop()
