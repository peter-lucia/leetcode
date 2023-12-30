/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    visited := make(map[*ListNode]bool)
    visited[head] = true

    for ;head != nil; {
        head = head.Next
        if visited[head] {
            return true
        }
        visited[head] = true
    }
    return false
    
}
