//
//  MainTableViewController.swift
//  Lab2_TemplateApp
//
//  Created by Sebastian Ernst on 11/01/2019.
//  Copyright © 2019 KIS AGH. All rights reserved.
//

import UIKit

class MainTableViewController: UITableViewController {
    
    var messages: [Message] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // load data from server
        print("[*] reading data from server")
        var url = "https://home.agh.edu.pl/~ernst/shoutbox.php?secret=ams2018"
        // Asynchronous Http call to your api url, using URLSession:
        URLSession.shared.dataTask(with: URL(string: url)!) { (data, response, error) -> Void in
            // Check if data was received successfully
            if error == nil && data != nil {
                do {
                    // Convert to dictionary where keys are of type String, and values are of any type
                    let json = try JSONSerialization.jsonObject(with: data!, options: .mutableContainers) as! [String: Any]
                    // Access specific key with value of type String
                    let arr: NSArray = json["entries"] != nil ? json["entries"] as! NSArray : []
                    //print(arr)
                    let dateFormatter = DateFormatter()
                    dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
                    for item in arr {
                        var dict = item as! NSDictionary
                        let name = dict["name"] as! String
                        let message = dict["message"] as! String
                        let time = dict["timestamp"] as! String
                        let date = dateFormatter.date(from: time)!
                        /*print("-----------")
                        print(name)
                        print(message)
                        print(date)*/
                        let msg = Message(_author: name, _time: date, _content: message)
                        self.messages.append(msg)
                    }
                    print("[+] data read properly, records: " + String(self.messages.count))
                    DispatchQueue.main.async {
                        self.tableView.reloadData()
                    }
                } catch {
                    print("[-] data could not be read from the address " + url)
                    // Something went wrong
                }
            }
            }.resume()
    }
    
    @IBAction func refreshData(_ sender: Any) {
        // TODO: reload data from server
        self.tableView.reloadData()
    }
    
    @IBAction func addMessage(_ sender: Any) {
        let alertController = UIAlertController(title: "New message", message: "Please state your name ad message", preferredStyle: .alert)
        alertController.addTextField(configurationHandler: { textField in
            textField.placeholder = "Your name"
        })
        alertController.addTextField(configurationHandler: { textField in
            textField.placeholder = "Your message"
        })
        let sendAction = UIAlertAction(title: "Send", style: .default, handler: { action in
            let name = alertController.textFields?[0].text
            let message = alertController.textFields?[1].text
            // TODO: submit data to server
        })
        alertController.addAction(sendAction)
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: { _ in })
        alertController.addAction(cancelAction)
        self.present(alertController, animated: true)
    }
    
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // TODO: return actual number of messages instead of random value
        if section == 0 {
            return self.messages.count
        }
        else {
            return 0
        }
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "shoutboxItem", for: indexPath)
        if indexPath.section == 0 {
            // TODO: return actual data instead of random values
            let message = "This is a placeholder message " + String(indexPath.item)
            let sender = "Jane Doe"
            let timestamp = Date(timeIntervalSinceNow: -1.0 * Double(Int.random(in: 10...5000)))
            /*let components = Calendar.current.dateComponents([.hour, .minute, .second], from: timestamp, to: Date())
            let metadata = "by \(sender), \(components.hour!) hour(s), \(components.minute!) minute(s) and \(components.second!) second(s) ago"*/
            
            let msg = self.messages[indexPath.item] //Message(_author: sender, _time: timestamp, _content: message)
            cell.textLabel!.text = msg.getText()
            cell.detailTextLabel!.text = msg.getDetails()
        }
        return cell
    }
    
}
