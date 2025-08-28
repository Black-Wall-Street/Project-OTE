```mermaid
---
config:
  theme: redux
---
flowchart LR
 subgraph s1["Trading System"]
        n5["Financial Data Port"]
        n6["Broker Port"]
        n7["New Data Port"]
        subgraph s2["Trading Engine"]
                n9["Indicators"]
                n10["Strategies"]

  end
  end
    n6 --> n2["Broker"]
    n3["Financial Data"] --> n5
    n4["News Outlet"] --> n7
    n5 -- Bar Data --> s2
    n7 -- News Data --> s2
    s2 -- Orders --> n6
    n9 -- Signal --> n10
    